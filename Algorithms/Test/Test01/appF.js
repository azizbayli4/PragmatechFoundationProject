obj = {
  first: function () {
    console.log("First");
  },
  second: function () {
    console.log("Second");
  },
  third: function () {
    console.log("Third");
  },
};

obj.first().second().third();
//obj.second();
//obj.second().first();
