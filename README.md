# pipeline

An ETL (Extract, Transform, Load) pipeline that demonstrates three approaches to testing.
In each case, we patch a function.
The cases differ in the object that's returned by the patched function:

* an instance of a mock class that we created (a stub)
* an instance of the real class, but initialised for testing
* an instance of a mock class that `unittest.mock` created (a mock)

(The terms in parentheses are defined by Martin Fowler in "[Mocks Aren't Stubs][]".)

## The problem

Our ETL pipeline contains an `extract` function that sends a request to a REST API.
The response contains a JSON string.
We want to test the `extract` function,
but we don't want to depend upon the REST API.

## The three approaches

We're using [pytest][] to help us write small, readable tests.
**Our first approach** follows the advice given by the "[Monkeypatching returned objects: building mock classes][]" page of pytest's documentation.
We're happy with it, not least because we have 100% coverage!

Remembering that "Explicit is better than implicit"[^1],
we add a `transform` function to our ETL pipeline that transforms the objects contained within the deserialised JSON string into instances of a class that we created (`Book`).
We notice that the deserialised JSON string contains dates,
but represented as strings rather than as instances of `datetime.date`,
so we transform from strings to `datetime.date`s in the `transform` function, too.

Transforming from from one type to another type in the `transform` function makes us uneasy:
the call to `.json()` is already doing that in the `extract` function.
Wouldn't it be better to keep all the code that relates to deserialising the JSON string in one place?
`object_hook` to the rescue!

Or not.
Our mock class doesn't know what to do with `object_hook`,
which is why we no longer have 100% coverage.
**Our second approach** is to use an instance of the real class, but initialised for testing.
This allows us to keep all the code that relates to deserialising the JSON string in the `extract` function.

Finally, we hear London calling:
we've heard about mockist testing and also about classical testing.
Surely, we're not *classical*?

**Our third approach** is to use an instance of a mock class that [`unittest.mock`][] created (`MagicMock`).
I'm not a mockist, but I have been tempted by mockist testing:
this is my best effort, in other words.
I think it's consistent with "[Mocks Aren't Stubs][]".
Notice that we no longer have 100% coverage.

[Mocks Aren't Stubs]: https://martinfowler.com/articles/mocksArentStubs.html
[Monkeypatching returned objects: building mock classes]: https://docs.pytest.org/en/stable/how-to/monkeypatch.html#monkeypatching-returned-objects-building-mock-classes
[`unittest.mock`]: https://docs.python.org/3.12/library/unittest.mock.html#module-unittest.mock
[pytest]: https://docs.pytest.org/en/stable/

[^1]: `import this`
