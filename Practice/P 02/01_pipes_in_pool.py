v = int(input())  # obem basein
p1 = int(input())  # debit purva truba za 4as
p2 = int(input())  # debit vtora truba za 4as
h = float(input())  # 4asove na otsustvie na rabotnika

p1_done = p1 * h
p2_done = p2 * h

total_done = p1_done + p2_done

if total_done <= v:
    percent_filled = (total_done / v) * 100
    p1_pct = (p1_done / total_done) * 100
    p2_pct = (p2_done / total_done) * 100
    print(f'The pool is {percent_filled:.2f}% full. Pipe 1: '
          f'{p1_pct:.2f}%. Pipe 2: {p2_pct:.2f}%.')
elif total_done > v:
    overflow = total_done - v
    print(f"For {h} hours the pool overflows with {overflow} liters.")
