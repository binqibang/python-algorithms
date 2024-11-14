from typing import List


def restore_ip_addresses(s: str) -> List[str]:
    # 25525511135 255.255.11.135, 255.255.111.35
    ips = []
    SEG_CNT, MAX_SEG = 4, 255
    segs = [''] * 4
    n = len(s)

    def backtrack(idx: int, segs: List[str], seg_id: int):
        if seg_id == SEG_CNT:
            if idx == n:
                ip = '.'.join(segs)
                ips.append(ip)
            return

        if idx == n:
            return

        if s[idx] == '0':
            segs[seg_id] = '0'
            backtrack(idx + 1, segs, seg_id + 1)

        seg = 0
        for i in range(idx, n):
            digit = ord(s[i]) - ord('0')
            seg = seg * 10 + digit
            if 0 < seg <= MAX_SEG:
                segs[seg_id] = str(seg)
                backtrack(i + 1, segs, seg_id + 1)
            else:
                break

    backtrack(0, segs, 0)
    return ips


if __name__ == '__main__':
    # print('.'.join(['255', '34', '34', '1']))
    # print(ord('2') - ord('0'))
    print(restore_ip_addresses('0000'))
