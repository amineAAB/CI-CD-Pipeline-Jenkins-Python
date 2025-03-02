pipeline {
    agent any
    stages {
//        stage('Checkout') {
//            steps {
//                git branch: 'main', url:  'https://github.com/amineAAB/tp_git'
//            }
//        }
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_script.py'
            }
        }
    }
}
