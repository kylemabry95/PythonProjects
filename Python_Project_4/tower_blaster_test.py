from tower_blaster import *

import unittest

# create additional tests that you can think of to make sure that our program is running correctly.

class Test_tower_blaster(unittest.TestCase):

    def test_setup_bricks(self):

        # create main pile and discard pile using setup_bricks
        main_pile, discard_pile = setup_bricks()

        # manually create test main pile and test discard pile to compare with
        test_main_pile = [i for i in range(1, 61)]
        test_discard_pile = []

        # check that main_pile and discard_pile have the correct bricks, in order
        self.assertListEqual(test_main_pile, main_pile)
        self.assertListEqual(test_discard_pile, discard_pile)

    def test_shuffle_bricks(self):

        # manually create main pile and discard pile
        main_pile = [i for i in range(1, 61)]
        discard_pile = []

        # create test main pile and test discard pile by getting copies
        test_main_pile = main_pile.copy()
        test_discard_pile = discard_pile.copy()

        # shuffle main pile and discard pile using shuffle_bricks
        shuffle_bricks(main_pile)
        shuffle_bricks(discard_pile)

        # check lengths of main pile and discard pile
        self.assertTrue(len(main_pile) == 60)
        self.assertTrue(len(discard_pile) == 0)

        # check that main pile and discard pile still contain the same values, regardless of order
        self.assertCountEqual(test_main_pile, main_pile)
        self.assertCountEqual(test_discard_pile, discard_pile)
        
    def test_check_bricks(self):

        # manually create main pile and discard pile
        main_pile = [i for i in range(1, 61)]
        discard_pile = []

        # call check_bricks
        check_bricks(main_pile, discard_pile)

        # check that main pile and discard pile are the same
        self.assertTrue(len(main_pile) == 60)
        self.assertTrue(len(discard_pile) == 0)

        # we will test other scenarios, for example, what if the main pile has only 1 brick left?
        # what if the main pile is empty?

    def test_check_tower_blaster(self):

        # test stable tower
        tower = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(check_tower_blaster(tower))

        # reverse the order of the stable tower and see that we get false.
        new_tower = reverse_list(tower)

        self.assertFalse(check_tower_blaster(new_tower))

        # test unstable tower
        tower = [1, 11, 20, 33, 45, 41, 47, 50, 57, 59]
        self.assertFalse(check_tower_blaster(tower))

        # make another unstable tower and test.
        new_tower = reverse_list(tower)
        self.assertFalse(check_tower_blaster(new_tower))

        # we will also test other stable and unstable towers

    def test_get_top_brick(self):

        # manually create main pile of bricks
        main_pile = [i for i in range(60, 0, -1)]
        self.assertEqual(len(main_pile), 60)

        # check that top brick of main pile is 60
        self.assertEqual(60, get_top_brick(main_pile))

        # check that main pile was updated, after getting top brick
        new_main_pile = [i for i in range(59, 0, -1)]
        self.assertListEqual(new_main_pile, main_pile)

        # make sure that 59 is the next brick.
        self.assertEqual(59, get_top_brick(main_pile))
        # make sure that the main_pile was updated after getting the top brick
        self.assertEqual(len(main_pile), 58)

        # we will test other scenarios, like other specific top bricks on main pile
        #we will also test for specific top brick on the discard pile

    def test_deal_initial_bricks(self):

        # create main pile and discard pile using setup_bricks
        main_pile, discard_pile = setup_bricks()

        # shuffle bricks using shuffle_bricks
        shuffle_bricks(main_pile)

        # check size of main_pile
        self.assertTrue(len(main_pile) == 60)

        # deal bricks using deal_initial_bricks
        computer_bricks, user_bricks = deal_initial_bricks(main_pile)

        # check that computer has 10 bricks
        self.assertTrue(len(computer_bricks) == 10)

        # check that user has 10 bricks
        self.assertTrue(len(user_bricks) == 10)

        # check that main pile has 40 bricks left
        self.assertTrue(len(main_pile) == 40)

        # check that bricks in computer_bricks are no longer in main_pile
        for i in computer_bricks:
            self.assertNotIn(i, main_pile)

        # check that bricks in user_bricks are not longer in main_pile
        for i in user_bricks:
            self.assertNotIn(i, main_pile)

        # we will test other scenarios, for example, that the bricks in user_bricks are no longer in main_pile

    def test_add_brick_to_discard(self):

        # manually create test discard pile
        discard_pile = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

        # shuffle the discard pile to make things interesting.
        shuffle_bricks(discard_pile)

        self.assertEqual(len(discard_pile), 10)

        # add specific brick to top of discard
        add_brick_to_discard(20, discard_pile)

        # test new length of discard
        self.assertEqual(len(discard_pile), 11)

        # should have added brick to top of discard (0 index in list)
        top_discard = discard_pile[0]
        self.assertEqual(20, top_discard)

        # we will test other scenarios with other test discard piles
 
    def test_find_and_replace(self):

        # manually create test tower pile
        tower = [18, 9, 20, 1, 7, 42, 39, 38, 51, 45]
        new_brick = 30
        brick_to_be_replaced = 39

        # manually create test discard pile
        discard = []

        # find and replace brick_to_be_replaced with new_brick
        find_and_replace(new_brick, brick_to_be_replaced, tower, discard)

        # create new tower and new discard pile to compare with
        new_tower = [18, 9, 20, 1, 7, 42, 30, 38, 51, 45]
        new_discard = [39]

        # check that brick was replaced and placed on discard
        self.assertListEqual(new_tower, tower)
        self.assertListEqual(new_discard, discard)

    def test_computer_play(self):

        # create main pile and discard pile.
        main_pile, discard_pile = setup_bricks()
        # shuffle bricks using shuffle_bricks
        shuffle_bricks(main_pile)




        # testing some of the functions that I designed for this homework.

    def test_bricks_are_almost_same(self):

        # create tower, index and brick that was picked.
        tower = [1, 9, 20, 3, 7, 42, 39, 38, 51, 45]
        index = 0
        brick_picked = 1

        # Saves the boolean return from bricks_are_almost_same
        are_bricks_almost_same = bricks_are_almost_same(tower, index, brick_picked)

        # We know from visual inspection that at index 0, 1 in the tower is not within +/- 3 of 21.
        self.assertTrue(are_bricks_almost_same, True)

        brick_picked = 11
        are_bricks_almost_same = bricks_are_almost_same(tower, index, brick_picked)
        # now test that we can get false from the function.
        self.assertFalse(are_bricks_almost_same, False)


    def test_reverse_list(self):

        # create a list
        list = [18, 9, 20, 1, 7, 42, 39, 38, 51, 45]
        # This is the reverse of the top list, made manually.
        reversed_list = [45, 51, 38, 39, 42, 7, 1, 20, 9, 18]

        # now reverse the list.
        new_list = reverse_list(list)

        # make sure that the new list is in fact reversed.
        self.assertEqual(new_list, reversed_list)
        # make sure that the first element in each list is the same.
        self.assertTrue(new_list[0] == reversed_list[0])
        # make sure that the new list is different from the old list.
        self.assertFalse(new_list == list)



if __name__ == '__main__':
    unittest.main()

 # we will test other scenarios with other test towers and test discard piles -the Ta's

