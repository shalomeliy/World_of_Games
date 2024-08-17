pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shalomeliy/main_score'
        IMAGE_VERSION = '1.0'
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

        stage('Login to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: '27b5d903-83f4-4e88-bf7c-58d9b75a3245', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        if (isUnix()) {
                            sh "echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin"
                        } else {
                            bat "echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin"
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
                            sh "docker-compose up --build -d"
                        } else {
                            bat "docker-compose up --build -d"
                            bat "docker ps -a"
                        }
                    }
                }
            }
        }

        stage('Tag & Push Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker tag $DOCKER_IMAGE:$IMAGE_VERSION $DOCKER_IMAGE:$IMAGE_VERSION"
                        sh "docker push $DOCKER_IMAGE:$IMAGE_VERSION"
                    } else {
                        bat "docker tag $DOCKER_IMAGE:$IMAGE_VERSION $DOCKER_IMAGE:$IMAGE_VERSION"
                        bat "docker push $DOCKER_IMAGE:$IMAGE_VERSION"
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
