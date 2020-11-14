# This module is meant to be a driver that allows a blockchain to be saved
# to disk or some other data storage destination.
#
# The default storage format is shelve because it's easy
#

import shelve
from .block import *

class DB:

    def __init__(self, the_db):

        self.db_file = the_db

        self.db = shelve.open(self.db_file)

    def add_chain(self, the_chain):

        if not the_chain.verify():
            raise Exception("The chain failed to verify")

        the_block = the_chain.get_genesis()

        while(True):

            # We add these identifiers to avoid any possible collisions
            # where id is the same as a valid hash
            store_id = "id:" + the_block.get_id()
            store_hash = "hash:" + the_block.get_hash()

            self.db[store_id] = the_block.get_json()

            # We also need to store a mapping from the hash to the ID
            self.db[store_hash] = the_block.get_id()

            the_block = the_block.get_next()
            if the_block is None:
                # We're at the end
                break

    def close(self):
        self.db.close()

    def load_by_id(self, block_id):

        store_id = "id:" + block_id

        the_block = load_json(self.db[store_id])
        return the_block

    def load_by_hash(self, block_hash):

        store_hash = "hash:" + block_hash
        the_id = self.db[store_hash]

        return self.load_by_id(the_id)