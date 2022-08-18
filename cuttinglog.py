def cut_log(p,  n,memo = {}):
    if (n == 0): return 0
    if n in memo.keys(): return memo[n]
    q = -1
    for i in range(1, n+1): 
        q = max(q, p[i] + cut_log(p, n - i, memo))
        # print(n, q)
    # print(memo)
        memo[n] =q
    return q

p = [0, 8, 17, 23, 25, 32, 34, 37, 46, 56, 57, 64, 66, 70, 78, 82, 92, 93, 96, 100, 110, 112, 118, 123, 124, 126, 133, 140, 144, 152, 157, 158, 167, 177, 183, 193, 199, 205, 209, 213, 215, 220, 223, 224, 229, 236, 238, 246, 255, 261, 263, 265, 269, 277, 284, 290, 299, 300, 307, 309, 314, 322, 328, 337, 343, 349, 355, 365, 369, 372, 374, 383, 388, 394, 397, 407, 416, 420, 425, 426, 436, 446, 452, 459, 467, 476, 484, 491, 493, 502]
p1 = [0, 9, 14, 21, 26, 35, 37, 45, 51, 53, 55, 61, 63, 65, 68, 78, 81, 89, 94, 100, 104, 112, 122, 125, 133, 134, 144, 151, 156, 164, 172, 180, 189, 192, 200, 203, 213, 222, 226, 229, 237, 239, 242, 247, 250, 252, 257, 263, 264, 269, 278, 283, 291, 296, 302, 307, 309, 315, 325, 335, 337, 343, 347, 353, 356, 362, 363, 368, 369, 376, 380, 383, 393, 402, 412, 419, 422, 426, 429, 432, 441, 448, 456, 463, 465, 471, 472, 476, 482, 483, 490, 497, 507, 511, 513, 516, 526, 533]
p2 = [0, 6, 8, 18, 20, 24, 31, 40, 46, 54, 62, 64, 65, 74, 84, 92, 97, 105, 113, 120, 121, 129, 134, 143, 151, 152, 154, 161, 163, 167, 175, 179, 187, 196, 203, 212, 217, 224, 226, 229, 230, 233, 235, 237, 238, 240, 245, 247, 256, 265, 272, 273, 282, 286, 294, 297, 304, 310, 314, 320, 321, 330, 334]
print(cut_log(p2,6))