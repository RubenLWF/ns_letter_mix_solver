# ns_letter_mix_solver
NS puts a game on the screens in their trains to find the station from the mixed letters.

These games look like this:
![alt text](<assets/example.jpg>)

---

Solving them is very easy.

Just put how often each letter occurs in a dictionary of the following structure: `{ letter : occurence_count }`.

Next do this for a list of all NS stations and see which one matches.

---

The result for the example is "Amsterdam Bijlmer ArenA".
