pipeline {
    agent any
    stages {
        stage("Check Jenkins") {
            steps {
                echo "Start.."
            }
        }
        stage("Deploy Test Envi") {
            steps {
                build 'flask-instance-deployer'
            }
        }

        stage("BVT Test") {
            steps {
                build 'flask-bvt-test'
            }
        }

        stage("Prod Step") {
            steps {
                echo "You can continue"
            }
        }
    }
}