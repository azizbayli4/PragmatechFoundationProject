obj = {
  first: function () {
    console.log("First");
    return obj;
  },
  second: function () {
    console.log("Second");
    return obj;
  },
  third: function () {
    console.log("Third");
    return obj;
  },
};

obj.first().second().third();
