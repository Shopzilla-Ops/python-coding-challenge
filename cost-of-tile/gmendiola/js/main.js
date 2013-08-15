function mainController($scope) {

    $scope.totalCost = function() {
        return $scope.height * $scope.height * $scope.price;
    };

}
