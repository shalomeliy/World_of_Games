pipeline {
    agent any

    environment {
        IMAGE_NAME_TAG = 'shalomeliy/main_score'
        // IMAGE_TAG will be set dynamically in the pipeline
    }

    stages {
        stage('Clean Up') {
            steps {
                deleteDir()
            }
        }
        stage('Clone Repo') {
            steps {
                script {
                    if (isUnix()) {
                        sh "git clone https://github.com/shalomeliy/World_of_Games.git"
                    } else {
                        bat "git clone https://github.com/shalomeliy/World_of_Games.git"
                    }
                }
            }
        }
        
        stage('Get Current Version') {
            steps {
                dir('World_of_Games') {
                    script {
                        def versionFile = readFile('version.txt').trim()
                        env.IMAGE_TAG = versionFile
                    }
                }
            }
        }
        
        stage('Increment Version') {
            steps {
                dir('World_of_Games') {
                    script {
                        def versionFile = readFile('version.txt').trim()
                        def newVersion = (versionFile.toInteger() + 1).toString()
                        writeFile file: 'version.txt', text: newVersion
                        env.IMAGE_TAG = newVersion
                    }
                }
            }
        }

        stage('Install Requirements') {
            steps {
                dir('World_of_Games') {
                    script {
                        if (isUnix()) {
                            sh "pip install -r requirements.txt"
                        } else {
                            bat "pip install -r requirements.txt"
                        }
                    }
                }
            }
        }

        stage('Build Docker') {
            steps {
                dir('World_of_Games') {
                    script {
                        if (isUnix()) {
                            sh "docker build -t ${IMAGE_NAME_TAG}:${IMAGE_TAG} ."
                        } else {
                            bat "docker build -t ${IMAGE_NAME_TAG}:${IMAGE_TAG} ."
                        }
                    }
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                dir('World_of_Games') { // Ensure directory name matches the clone repo stage
                    script {
                        if (isUnix()) {
                            sh "docker-compose up -d"
                        } else {
                            bat "docker-compose up -d"
                        }
                    }
                }
            }
        }

        stage('E2E Test') {
            steps {
                dir('World_of_Games') {
                    script {
                        catchError(buildResult: 'FAILURE', stageResult: 'FAILURE') {
                            if (isUnix()) {
                                sh 'python tests/e2e.py'
                            } else {
                                bat 'python tests/e2e.py'
                            }
                        }
                    }
                }
            }
        }

        stage('Tag & Push Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker push ${IMAGE_NAME_TAG}:${IMAGE_TAG}"
                    } else {
                        bat "docker push ${IMAGE_NAME_TAG}:${IMAGE_TAG}"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                dir('World_of_Games') {
                    script {
                        if (isUnix()) {
                            sh 'docker-compose down'
                        } else {
                            bat 'docker-compose down'
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

