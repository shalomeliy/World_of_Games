pipeline {
    agent any

    environment {
        DOCKER_IMAGE_BASE = 'shalomeliy/world_of_games'
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
        stage('Increment Version') {
            steps {
                dir('World_of_Games') {
                    script {
                        def versionFile = readFile 'version.txt'
                        def versionNumber = versionFile.trim().toInteger()
                        versionNumber += 1
                        writeFile file: 'version.txt', text: versionNumber.toString()
                        env.VERSION = versionNumber.toString()
                        env.DOCKER_IMAGE = "${DOCKER_IMAGE_BASE}:${env.VERSION}"
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
                        }
                    }
                }
            }
        }
        stage('Tag & Push Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker tag ${DOCKER_IMAGE_BASE}:${env.VERSION} ${DOCKER_IMAGE_BASE}:latest"
                        sh "docker push ${DOCKER_IMAGE_BASE}:${env.VERSION}"
                        sh "docker push ${DOCKER_IMAGE_BASE}:latest"
                    } else {
                        bat "docker tag ${DOCKER_IMAGE_BASE}:${env.VERSION} ${DOCKER_IMAGE_BASE}:latest"
                        bat "docker push ${DOCKER_IMAGE_BASE}:${env.VERSION}"
                        bat "docker push ${DOCKER_IMAGE_BASE}:latest"
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
