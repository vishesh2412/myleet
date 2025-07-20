class Solution(object):
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0
        while i < len(words):
            # Determine how many words fit into the current line
            line_len = len(words[i])
            j = i + 1
            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            # Number of words in this line
            num_words = j - i
            # Number of spaces to distribute
            space_needed = maxWidth - line_len

            line = ""
            if j == len(words) or num_words == 1:
                # Last line or a line with one word - left justified
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                # Middle justified line
                spaces = space_needed // (num_words - 1)
                extra = space_needed % (num_words - 1)

                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (spaces + (1 if k - i < extra else 0))
                line += words[j - 1]  # last word in the line

            res.append(line)
            i = j
        return res
