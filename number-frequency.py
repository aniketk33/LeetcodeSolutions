'''Give a list of numbers, sort them descending by their frequeny. If there are multiple numbers with the same frequency then sort the numbers in ascending order'''

class Solution:
    
    def num_freq(self, nums):
        freq_dict = {}
        self.repeated_freq = []
        result = []
        for i in nums:
            if i not in freq_dict.keys():
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1

        # getting repeated freqquency list
        freq_dict_values = [val for val in freq_dict.values()]
        for i in range(len(freq_dict_values)):
            for j in range(i+1, len(freq_dict_values)):
                if freq_dict_values[i] != freq_dict_values[j]:
                    continue
                self.repeated_freq.append(freq_dict_values[i])
                break

        
        self.freq_dict = freq_dict
        recent_duplicate_added = 0
        for key, val in freq_dict.items():
            # in order to prevent adding the same key in the final result the check is added
            if val == recent_duplicate_added:
                continue
            if val in self.repeated_freq:
                recent_duplicate_added = val
                sorted_keys = self.sort_keys(val)
                for key in sorted_keys:
                    temp_list = [key, val]
                    result.append(temp_list)
            else:    
                temp_list = [key, val]
                result.append(temp_list)
        
        return result

    def sort_keys(self, value):
        return sorted([key for key, val in self.freq_dict.items() if val == value])
        



input = [3,1,2,1,3]
result = Solution().num_freq(input)