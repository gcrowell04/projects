import datetime
import hashlib
import json
import flask
from flask import jsonify, Flask


class Blockchain():
    
    def init(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
        
        # Add blocks to the chain
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                     'timestamp': str(datetime.datetime.now()),
                     'proof': proof,
                     'previous_hash': previous_hash}
        self.chain.append(block)
        return block
        
        # Display previous block
    def print_previous_block(self):
        return self.chain[-1]
            
        # Mine the block
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
            
        while check_proof is False:
            hash_op = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_op[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
            
        return new_proof
        
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
        
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index  = 1
            
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.has(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
                
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
                
        return True

app = Flask(__name__)

blockchain = Blockchain()

# Mine a new block
@app.route('/mine_block', methods=['POST', 'GET'])
def mine_block():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof,previous_hash)
    
    response = {'message': 'a Block is MINED',
                'index' : block['index'],
                'timestamp' : block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    
    return jsonify(response), 200


# Display blockchain in json
@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Check validity of blockchain
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
    
    if valid:
        response = {'message': 'Valid Blockchain'}
    else:
        reponse = {'message': 'Invalid Blockchain'}
        
    return jsonify.response(response), 200

# Run Flask locally
blockchain.init()
app.run(host='127.0.0.1', port=5000)    
        
