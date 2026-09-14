pipeline {
    agent any

    stages {
        stage('Check Files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Test Application') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }

        stage('Run Application') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
