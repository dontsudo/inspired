// 🏄‍♂️ NProgress
NProgress.start();
NProgress.set(0.4);

var interval = setInterval(function () {
  NProgress.inc();
}, 1000);

$(document).ready(function () {
  NProgress.done();
  clearInterval(interval);
});
