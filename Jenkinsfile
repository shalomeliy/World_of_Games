pipeline {
    agent any

    environment {
        DOCKER_IMAGE_BASE = 'shalomeliy/world_of_games'
        VERSION = '' // Initialize the version variable
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
                        env.VERSION = versionNumber.toString() // Save the version to environment variable
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
                    def dockerTag = "${DOCKER_IMAGE_BASE}:${env.VERSION}"
                    def dockerLatestTag = "${DOCKER_IMAGE_BASE}:latest"

                    if (isUnix()) {
                        sh "docker tag ${DOCKER_IMAGE_BASE} ${dockerTag}"
                        sh "docker push ${dockerTag}"
                        sh "docker tag ${DOCKER_IMAGE_BASE} ${dockerLatestTag}"
                        sh "docker push ${dockerLatestTag}"
                    } else {
                        bat "docker tag ${DOCKER_IMAGE_BASE} ${dockerTag}"
                        bat "docker push ${dockerTag}"
                        bat "docker tag ${DOCKER_IMAGE_BASE} ${dockerLatestTag}"
                        bat "docker push ${dockerLatestTag}"
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
