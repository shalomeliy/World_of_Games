pipeline {
    agent any

    environment {
        VERSION_FILE = 'World_of_Games/version.txt'
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

        stage('Read and Increase Version Number') {
            steps {
                script {
                    // Read current version number
                    def currentVersionNumber = readFile(VERSION_FILE).trim().toInteger()

                    // Increment the version number
                    def newVersionNumber = currentVersionNumber + 1
                    
                    // Write the new version number back to the file
                    writeFile file: VERSION_FILE, text: "${newVersionNumber}"
                    
                    // Set the new version number as an env. variable for Docker tag
                    env.IMAGE_VERSION = newVersionNumber.toString()
                    env.IMAGE_TAG = newVersionNumber.toString()
                    
                    echo "Updated version to: ${env.IMAGE_VERSION}"
                    
                }
            }
        }

        stage('Build Docker') {
            steps {
                dir('World_of_Games') {
                    script {
                        echo "Building Docker image with version: ${env.IMAGE_VERSION}"
                        if (isUnix()) {
                            sh "docker build -t ${DOCKER_IMAGE_BASE}:${env.IMAGE_VERSION} ."
                        } else {
                            bat "docker build -t ${DOCKER_IMAGE_BASE}:${env.IMAGE_VERSION} ."
                            bat "docker images"
                        }
                    }
                }
            }
        }

        stage('Docker Compose Up') {
            steps {
                dir('World_of_Games') {
                    script {
                        if (isUnix()) {
                            sh "docker-compose up -d"
                        } else {
                            bat "docker-compose up -d"
                            bat "docker ps"
                        }
                    }    
                }
            }
        }

               stage('E2E Test') {
            steps {
                dir('World_of_Games') {
                    script {
                            if (isUnix()) {
                                sh 'python tests/e2e.py'
                            } else {
                                bat 'python tests/e2e.py'
                        }
                    }
                }
            }
        }

//        stage('Tag & Push Docker Image') {
//            steps {
//                script {
//                    if (isUnix()) {
//                        sh "docker tag ${DOCKER_IMAGE_BASE}:${env.IMAGE_VERSION} ${DOCKER_IMAGE_BASE}:latest"
//                        sh "docker push ${DOCKER_IMAGE_BASE}:${env.IMAGE_VERSION}"
//                        sh "docker push ${DOCKER_IMAGE_BASE}:latest"
//                    } else {
//                        bat "docker tag ${DOCKER_IMAGE_BASE}:${env.IMAGE_VERSION} ${DOCKER_IMAGE_BASE}:latest"
//                        bat "docker push ${DOCKER_IMAGE_BASE}:${env.IMAGE_VERSION}"
//                        bat "docker push ${DOCKER_IMAGE_BASE}:latest"
//                    }
//                }
//            }
//        }
        stage('Push Docker Image') {
                steps {
                    script {
                        // Tag and push the Docker image with the new build number
                         if (isUnix()) {
                             sh "docker push ${DOCKER_IMAGE_BASE}:${env.IMAGE_VERSION}"
                        } else {
                             bat "docker push ${DOCKER_IMAGE_BASE}:${env.IMAGE_TAG}"
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
