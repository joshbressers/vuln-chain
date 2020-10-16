import unittest
import dwf_chain


class TestBlock(unittest.TestCase):

    def test_create(self):
        the_block = dwf_chain.Block('id', 0, 'prev_hash', 'hash')

        self.assertEqual(the_block.get_date(), 0, "Should be 0")
        self.assertEqual(the_block.get_id(), 'id', "Should be 'id'")
        self.assertEqual(the_block.get_prev_hash(), 'prev_hash', "Should be 'prev_hash'")
        self.assertEqual(the_block.get_hash(), 'hash', "Should be 'hash'")

    def test_hash(self):

        hash = "ec81332e528ff522bfb05e93cd826c075ec26c5b9cc5bfcf7087d6f28da90e1d4f44df2a9af32573df5ab535d4b985731001c71d9f7629170518bba95280ef3d"

        the_block = dwf_chain.Block('id', 0, 'prev_hash')
        output = the_block.gen_hash()

        self.assertEqual(output, hash, "Should be '%s'" % hash)

    def test_verify(self):

        hash = "ec81332e528ff522bfb05e93cd826c075ec26c5b9cc5bfcf7087d6f28da90e1d4f44df2a9af32573df5ab535d4b985731001c71d9f7629170518bba95280ef3d"

        the_block = dwf_chain.Block('id', 0, 'prev_hash', hash)

        self.assertTrue(the_block.verify())

        the_block = dwf_chain.Block('id', 0, 'prev_hash', 'bad_hash')
        self.assertFalse(the_block.verify())

if __name__ == '__main__':
    unittest.main()

