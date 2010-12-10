import unittest

import snail



class testBlogger(unittest.TestCase):

    """

    A test class for the Blogger module.

    """



    def setUp(self):

        """

        set up data used in the tests.

        setUp is called before each test function execution.

        """

        self.snail = Blogger.get_blog()



    def testGetFeedTitle(self):

        title = "fitnessetesting"

        self.assertEqual(self.blogger.get_title(), title)



    def testGetFeedPostingURL(self):

        posting_url = "http://www.blogger.com/atom/9276918"

        self.assertEqual(self.blogger.get_feed_posting_url(), posting_url)



    def testGetFeedPostingHost(self):

        posting_host = "www.blogger.com"

        self.assertEqual(self.blogger.get_feed_posting_host(), posting_host)



    def testPostNewEntry(self):

        init_num_entries = self.blogger.get_num_entries()

        title = "testPostNewEntry"

        content = "testPostNewEntry"

        self.assertTrue(self.blogger.post_new_entry(title, content))

        self.assertEqual(self.blogger.get_num_entries(), init_num_entries+1)

        # Entries are ordered most-recent first

        # Newest entry should be first

        self.assertEqual(title, self.blogger.get_nth_entry_title(1))

        self.assertEqual(content, self.blogger.get_nth_entry_content_strip_html(1))



    def testDeleteAllEntries(self):

        self.blogger.delete_all_entries()

        self.assertEqual(self.blogger.get_num_entries(), 0)



def suite():

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(testBlogger))

    return suite



if __name__ == '__main__':

    #unittest.main()



    suiteFew = unittest.TestSuite()

    suiteFew.addTest(testBlogger("testPostNewEntry"))

    suiteFew.addTest(testBlogger("testDeleteAllEntries"))

    #unittest.TextTestRunner(verbosity=2).run(suiteFew)

    unittest.TextTestRunner(verbosity=2).run(suite())
