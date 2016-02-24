(function(){
var app= angular.module('account', [])
.controller('accountcontroller', ['$scope', function($scope) {
  $scope.account = {
          input:"input",
          output:function(){
                     var accountObject;
                     accountObject = $scope.account;
                     return accountObject.input ;


                    }
                   };
}]);
})();


