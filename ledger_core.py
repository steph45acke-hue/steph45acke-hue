import hashlib
import mysql.connector
from datetime import datetime

#establishing my connection to my SQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="stephen0111301468",
    database="tamper_evident_ledger"
)

cursor = db.cursor()
# function to create a secure SHA-256 cryptographic hash
def calculate_hash(previous_hash,data_string,nonce):
    #combine everything into a single string
    block_content = f"{previous_hash}{data_string}{nonce}"
    #encrypt it using # SHA-256 and return the 64-character fingerprint
    return hashlib.sha256(block_content.encode()).hexdigest()

# function to create and insert the genesis block into my SQL
def create_genesis_block():
 previous_hash = "0" * 64
 genesis_data = "Genesis Block - system initialized" 
 nonce = 0

def create_genesis_block():
    previous_hash = "0" * 64
    genesis_data = "Genesis Block - system initialized" 
    nonce = 0
    
    # Generate the cryptographic hash for this block using our function
    block_hash = calculate_hash(previous_hash, genesis_data, nonce)
    
    # Insert the block header into our MySQL 'ledger_blocks' table
    block_query = "INSERT INTO ledger_blocks (previous_hash, block_hash, nonce) VALUES (%s, %s, %s)"
    cursor.execute(block_query, (previous_hash, block_hash, nonce))
    db.commit()
    
    # Get the unique ID of the block we just created
    block_id = cursor.lastrowid 
    
    # Insert a dummy transaction into 'ledger_transactions' linking it to this block via foreign key
    tx_query = "INSERT INTO ledger_transactions (block_id, sender_name, receiver_name, amount) VALUES (%s, %s, %s, %s)"
    cursor.execute(tx_query, (block_id, "System", "Ledger Initialized", 0.00))
    db.commit()
    
    print(f"Genesis Block successfully created and stored! Block Hash: {block_hash}")

# Run the function when we execute this script
if __name__ == "__main__":
    create_genesis_block()

def add_block(sender, receiver, amount):
    # 1. Fetch the hash of the most recent block from the database to use as previous_hash
    cursor.execute("SELECT block_hash FROM ledger_blocks ORDER BY block_id DESC LIMIT 1;")
    last_block = cursor.fetchone()
    
    if last_block:
        previous_hash = last_block[0]
    else:
        previous_hash = "0" * 64

    # 2. Define block data and calculate the new block's hash
    block_data = f"Transaction: {sender} to {receiver} for {amount}"
    nonce = 0
    block_hash = calculate_hash(previous_hash, block_data, nonce)
    
    # 3. Insert the new block header into 'ledger_blocks'
    block_query = "INSERT INTO ledger_blocks (previous_hash, block_hash, nonce) VALUES (%s, %s, %s)"
    cursor.execute(block_query, (previous_hash, block_hash, nonce))
    db.commit()
    
    # 4. Get the new block's ID and link the transaction
    block_id = cursor.lastrowid
    tx_query = "INSERT INTO ledger_transactions (block_id, sender_name, receiver_name, amount) VALUES (%s, %s, %s, %s)"
    cursor.execute(tx_query, (block_id, sender, receiver, amount))
    db.commit()
    
    print(f"New Block added successfully! Hash: {block_hash[:16]}... linked to previous block.")

if __name__ == "__main__":
    # Create genesis block if table is empty, then add a test transaction block
    add_block("Alice", "Bob", 150.00)
    

    