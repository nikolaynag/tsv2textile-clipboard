#!/usr/bin/env python
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


def tsv2textile(text):
    rows = []
    for line in text.split("\n"):
        row = line.split("\t")
        rows.append(row)

    colSizes = {}
    for row in rows:
        for i, v in enumerate(row):
            cnt = len(v)
            size = colSizes.get(i, 0)
            if size < cnt:
                colSizes[i] = cnt

    output = []
    for n, row in enumerate(rows):
        if n == 0:
            delim = u"|_. "
        else:
            delim = u"|   "
        cells = [
            v.ljust(colSizes[i] + 2)
            for i, v in enumerate(row)
        ]
        output.append(u"{} {} |".format(delim, delim.join(cells)))

    return "\n".join(output)


def main():
    window = tk.Tk()
    window.withdraw()
    text = window.clipboard_get()
    window.clipboard_append(tsv2textile(text))
    window.after(2000, window.destroy)
    window.mainloop()

if __name__ == "__main__":
    main()
