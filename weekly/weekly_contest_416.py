from typing import List
import heapq


class WeeklyContest416:
    def report_spam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        banner_words_set = set(bannedWords)
        for word in message:
            if word in banner_words_set:
                count += 1
            if count >= 2:
                break
        return count >= 2

    def min_number_of_seconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        min_heap = []
        for t in workerTimes:
            # total_time, time, count
            heapq.heappush(min_heap, (t, t, 1))
        ans = 0
        while mountainHeight > 0:
            total_time, time, count = heapq.heappop(min_heap)
            mountainHeight -= 1
            ans = max(ans, total_time)
            count += 1
            total_time += count * time
            heapq.heappush(min_heap, (total_time, time, count))
        return ans

    def valid_substring_count(self, word1: str, word2: str) -> int:
        # "bcca" "abc"
        n1, n2 = len(word1), len(word2)
        if n1 < n2:
            return 0
        letter_cnt_1, letter_cnt_2 = [0] * 26, [0] * 26
        for letter in word2:
            letter_cnt_2[ord(letter) - ord('a')] += 1

        start, end = 0, len(word2) - 1
        ans = 0

        for i in range(start, end + 1):
            letter_cnt_1[ord(word1[i]) - ord('a')] += 1

        while end < n1:
            if self.check(letter_cnt_1, letter_cnt_2):
                ans += n1 - end
                letter_cnt_1[ord(word1[start]) - ord('a')] -= 1
                start += 1
            else:
                if end < n1 - 1:
                    end += 1
                    letter_cnt_1[ord(word1[end]) - ord('a')] += 1
                else:
                    break
        return ans

    def check(self, cnt1: List[int], cnt2: List[int]) -> bool:
        for i in range(len(cnt1)):
            if cnt1[i] < cnt2[i]:
                return False
        return True


if __name__ == '__main__':
    w = WeeklyContest416()
    print(w.valid_substring_count("bbb", "bc"))
    print(w.min_number_of_seconds(10, [3, 2, 2, 4]))
