type ReturnObj = {
  increment: () => number;
  decrement: () => number;
  reset: () => number;
};

function createCounter(init: number): ReturnObj {
  let currentCount = init;

  return {
    increment: function () {
      currentCount += 1;
      return currentCount;
    },
    decrement: function () {
      currentCount -= 1;
      return currentCount;
    },
    reset: function () {
      currentCount = init;
      return currentCount;
    },
  };
}

/*
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
