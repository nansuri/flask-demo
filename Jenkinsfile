pipeline {
    agent any
    stages {
        stage("Check Jenkins") {
            steps {
                echo "Start.."
            }
        }
        stage("Deploy Staging") {
            steps {
                build 'flask-instance-deployer'
            }
        }

        stage("BVT Test") {
            steps {
                build 'flask-bvt-test'
            }
        }
    }
}