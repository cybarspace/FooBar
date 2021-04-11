# FooBar module

## The performance of a dictionary at the convenience of a list

### Features:

*(or bugs...)*

- Provides a `function` and a `Class`
- The `function` takes an arbitrary number of `arguments` and returns a dictionary where the keys are numbers starting at `0` (like list indices).
- The `Class` takes a `list` or `tuple` and *holds* the values in a “private” `dict` produced by the `function` above
- Uses `dataclasses` for the `Class`
- Uses a `dict` for the `function`
- The `function` provides a speedup of nearly `50%` but has no type checks or anything to discourage modification of data, since it *just* returns a `dict`. The `Class` is a joke. Use a `tuple` for better performance and “safety”.

### The Quest for FooBar

**TL;DR** - use this:

```python
def foobar(*__baz): return dict(enumerate(__baz))

fb = foobar(
    "foo",
    "bar",
    "baz"
)

print(fb)
# output: {0: 'foo', 1: 'bar', 2: 'baz'}
```

*Now, onto the real story...*

All over the internet, I saw the words `foo`, `bar` and `baz`. Sometimes as `foobar`, other times, as separate words. I searched far and wide - “What is this mysterious foobar they speak of?” But alas, I found nothing. Frustrated, I sat down before my ancient weapon - a Dell Inspiron from half-a-decade ago - and started typing furiously on its keyboard. I coded and I [Ecosia](https://www.ecosia.org/)-ed for a solution. I was open - no idea was a bad idea, and any light of hope in this sea of despair would be showered with gratitude. Minutes turned to hours. Hours to days, days to weeks.

Finally, two months later, just as I was about to give up, Big Brother YouTube suggested me [a video](https://youtu.be/vBH6GRJ1REM). I watched eagerly - though I was careful not to get my hopes too high, lest I be disappointed - and soon, my frown slowly turned into a smile. I had found it - the solution to my life’s problems. I was enlightened with the knowledge of `dataclasses` - a language feature introduced in `Python 3.7`. Armed with this newfound magic amulet, I approached the humongous albeit practically useless spaghetti code I had produced in my frantic desperation. With a heavy heart, I pressed `Ctrl+A` and then, `Backspace` - it was gone. It was time to start anew. With renewed vigour and hope, I typed away. In an hour I was able to code a working model. It was far from perfect, but it was small, simple and most importantly - it worked! I was filled with joy. A blend of dopamine and oxytocin flushed through me, warming up my chest with a tingle. But I knew there was more work to be done - this was not the end.

My initial idea that failed was to use a linked list so that it performed better than Python lists. I didn’t know about `dataclasses` at the time, it was too messy, confusing and much slower than lists. So now after I implemented a more simple data type using `dataclasses`, I thought of finding a functional solution to the problem - one that doesn’t have as much type checking and “safety” mechanisms in place, but one that creates and returns a `dict` directly. My first version just took the post-init mechanism of the `Class` implementation and put it in a function. It worked, but it was bigger than it needed to be. Less verbose and beginner-friendly, but not as memeworthy. During my conquests, I took a lot of help from the good folks at [CS Dojo’s Discord server](https://csdojo.io/d), so I turned to them for guidance yet again. A mentor there, `enilator`, [suggested a shorter way](https://discord.com/channels/502519660726714378/510472371312918537/830045983085821983) using `enumatate`. I had no idea how that worked (and I still don’t), but I implemented it. A few minutes later I realized that I can increase the meme-worthiness of it all by putting it into a `lambda` expression and assigning it to a variable (which is strongly discouraged in Python). After doing that, I commented it out and went back to the `def` function to comply with *The Zen of Python*.

And that is how I found the light - the light of FooBar.