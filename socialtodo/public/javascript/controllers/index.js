angularapp
    .controller('toast', function($scope) {

    var last = {
      bottom: false,
      top: true,
      left: false,
      right: true
    };

    $scope.showSimpleToast = function() {
    $mdToast.show(
      $mdToast.simple()
        .textContent('Simple Toast!')
        .position(last)
        .hideDelay(3000)
        );
    };
    })