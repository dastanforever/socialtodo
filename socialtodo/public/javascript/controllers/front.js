angularapp
  	.controller('navmenu', function($scope, $mdDialog){

  		this.showlogin = function (ev) {
  		$mdDialog.show({

  			controller: DialogController,
      		templateUrl: 'dialogs/loginDialog.tmpl.html',
      		parent: angular.element(document.body),
      		targetEvent: ev,
      		clickOutsideToClose:true
    	})       
        .then(function(answer) {
          $scope.status = 'You said the information was "' + answer + '".';
        	}, function() {
          $scope.status = 'You cancelled the dialog.';
        });
    }

  	})

  	.controller('form', function($scope) {
      	$scope.submit = 'register';
    	$scope.user = {
      		username: '',
      		email: '',
      		firstName: '',
      		lastName: '',
      		password: '',
    		};

    	$scope.changesubmit = function (str) {
    		$scope.submit = str;
    	}
      })


function DialogController($scope, $mdDialog) {
  $scope.hide = function() {
    $mdDialog.hide();
  };
  $scope.cancel = function() {
    $mdDialog.cancel();
  };
  $scope.answer = function(answer) {
    $mdDialog.hide(answer);
  };
}