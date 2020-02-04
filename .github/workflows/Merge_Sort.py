

class merge_sort():

    def __init__(self):
        """
        This class is to perform Merge Sort on a given List/Array
        """
        self.verified = False
        self.getSorted = []

    def _verify_array(self, list_to_sort):
        """
        This method is used for verifing either array contain invalid entries.
        """
        try:
            for element in list_to_sort:
                int(element)
        except:
            exit('Please input a valid numerical values')



    def sort(self, list_to_sort):
        """ This method is used to sort the given array
        """
        # Verify
        if self.verified is False:
            self._verify_array(list_to_sort)
            self.verified = True

        # Divide
        if len(list_to_sort) >= 2:
            middle_marker = (len(list_to_sort)) // 2
            left_list = list_to_sort[0:middle_marker]
            right_list = list_to_sort[middle_marker:]

            # Conquer
            self.sort(left_list)
            self.sort(right_list)
            # Merge
            self.merge(left_list, right_list, list_to_sort)


    def merge(self, left_list, right_list, list_to_sort):

        """ This method is used to merge the given array
        """
        pointer_left = 0
        pointer_right = 0
        pointer_in_array = 0

        # Comparing
        while (pointer_left < len(left_list)) and (pointer_right < len(right_list)):
            if left_list[pointer_left] <= right_list[pointer_right]:
                list_to_sort[pointer_in_array] = left_list[pointer_left]
                pointer_in_array += 1
                pointer_left += 1
            else:
                list_to_sort[pointer_in_array] = right_list[pointer_right]
                pointer_in_array += 1
                pointer_right += 1

        # Collecting leftovers
        while pointer_left < len(left_list):
            list_to_sort[pointer_in_array] = left_list[pointer_left]
            pointer_in_array += 1
            pointer_left += 1

        # Collecting leftovers
        while pointer_right < len(right_list):
            list_to_sort[pointer_in_array] = right_list[pointer_right]
            pointer_in_array += 1
            pointer_right += 1

        self.getSorted = list_to_sort





