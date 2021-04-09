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
```

*Now, onto the real story...*

All over the internet, I saw the words `foo`, `bar` and `baz`. Sometimes as `foobar`, other times, as separate words. I searched far and wide - “What is this mysterious foobar they speak of?” But alas, I found nothing. Frustrated, I sat down before my ancient weapon - a Dell Inspiron from half-a-decade ago - and started typing furiously on its keyboard. I coded and I [Ecosia](https://www.ecosia.org/)-ed for a solution. I was open - no idea was a bad idea, and any light of hope in this sea of despair would be showered with gratitude. Minutes turned to hours. Hours to days, days to weeks.

Finally, two months later, just as I was about to give up, Big Brother YouTube suggested me [a video](https://youtu.be/vBH6GRJ1REM). I watched eagerly - though I was careful not to get my hopes too high, lest I be disappointed - and soon, my frown slowly turned into a smile. I had found it - the solution to my life’s problems. I was enlightened with the knowledge of `dataclasses` - a language feature introduced in `Python 3.7`. Armed with this newfound magic amulet, I approached the humongous albeit practically useless spaghetti code I had produced in my frantic desperation. With a heavy heart, I pressed `Ctrl+A` and then, `Backspace` - it was gone. It was time to start anew. With renewed vigour and hope, I typed away. In an hour I was able to code a working model. It was far from perfect, but it was small, simple and most importantly - it worked! I was filled with joy. A blend of dopamine and oxytocin flushed through me, warming up my chest with a tingle. But I knew there was more work to be done - this was not the end.

*To be continued...*

