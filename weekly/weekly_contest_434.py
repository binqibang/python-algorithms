from typing import List


class WeeklyContest434:
    def count_partitions(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        left_sum, right_sum = 0, total
        count = 0
        for i in range(n - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if (left_sum - right_sum) % 2 == 0:
                count += 1
        return count

    def count_mentions(
        self, number_of_users: int, events: List[List[str]]
    ) -> List[int]:
        ans = [0] * number_of_users
        # sort events by event[1], if event[1] is the same, sort by descending event[0]
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))
        last_offline_time = [-1] * number_of_users
        for event in events:
            curr_time = int(event[1])
            if event[0] == "MESSAGE":
                if event[2] == "ALL":
                    for i in range(number_of_users):
                        ans[i] += 1
                elif event[2] == "HERE":
                    for i in range(number_of_users):
                        if (
                            last_offline_time[i] == -1
                            or curr_time - last_offline_time[i] >= 60
                        ):
                            ans[i] += 1
                else:
                    for id in event[2].split(" "):
                        ans[int(id[2:])] += 1
            else:
                id = int(event[2])
                last_offline_time[id] = curr_time
        return ans


if __name__ == "__main__":
    algo = WeeklyContest434()
    print(algo.count_partitions([10, 10, 3, 7, 6]))
    print(
        algo.count_mentions(
            5,
            [
                ["OFFLINE", "28", "1"],
                ["OFFLINE", "14", "2"],
                ["MESSAGE", "2", "ALL"],
                ["MESSAGE", "28", "HERE"],
                ["OFFLINE", "66", "0"],
                ["MESSAGE", "34", "id2"],
                ["MESSAGE", "83", "HERE"],
                ["MESSAGE", "40", "id3 id3 id2 id4 id4"],
            ],
        )
    )
