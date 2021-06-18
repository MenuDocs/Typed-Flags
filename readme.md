Typed Flags
---

A Typehint based system for including flag input in your discord.py commands.

Why bother with numerous decorators and patched commands when you just typehint your input to receive command flags?

#### Examples

Usage is as simple as typehinting the entire input argument string to `TypedFlags`, this in turn will convert everything and will return this argument as a `dict` of `key:value` pairs where each `key` is the flag, and the `value` is the value for that flag

```python
@bot.command()
async def test(ctx, *, args: TypedFlags):
    # Send all of command args
    await ctx.send(args)
```
An example calling the above code:
`%test this "Lol ez" --try:="test string" --hard:=This is "kinda cool"`
```python
args = {'argless': ['this', 'Lol ez', 'is', 'kinda', 'cool'], 'try': 'test string', 'hard': 'This'}
```


#### Customization

You can customize two things, the string to preceed any flag values as well as the string to split up between the flag and its value.
Both of these are keyword arguments when initializing `TypedFlags`

- `start`: str -> The string to preceed any flags (Defaults to `--`)
- `delim`: str -> What to split flags with to get the `key:value` split (Defaults to `:=`)
- `suppress_reserved_keyword`: boolean -> Whether to suppress errors on reserved keywords (Defaults to `False`)
    - Currently `argless` is reserved
    - By default, if the user provides a flag called `argless` it raises `ReservedKeyword` 
    - If you set this to `True` it will overwrite `argless`, this does mean you lose any arguments without a flag

You do not have to provide these values. There are defaults in place. It is only for customization purposes

#### Important Notes

This package works in-line with how discord.py handles command parsing and consumption. That is to say the argument `Hello world` will be *two* variables, where as the argument `"Hello world"` will be parsed as one argument. This is something important to understand otherwise you will experience unexpected behaviour.


Any arguments **not** associated with a flag will be added to the dictionary under the key `argless`. The value for this key is a `list` containing all of the arguments found that do not corrospond to a given flag. 

It is **also** important to note that if no `argless` values are detected then this key *will not* be in the dictionary. You should check for this in your code.
