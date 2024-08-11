pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shalomeliy/main_score'
        DOCKER_REGISTRY = 'https://hub.docker.com/repository/docker/shalomeli/world_of_games/tags'
        VERSION = 'latest' // Default version, will be updated in the pipeline
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
      stage('Get Latest Tag and Set Version') {
        steps {
            script {
                try {
                    def response = sh(script: 'curl -s https://hub.docker.com/v2/repositories/shalomeliy/world_of_games/tags/', returnStdout: true).trim()
                    echo "Docker Hub response: ${response}"
                    def tags = readJSON(text: response)
                    def latestTag = tags.results[0]?.name ?: 'latest'
                    echo "Latest tag: ${latestTag}"
                    env.DOCKER_IMAGE_TAG = latestTag
                } catch (Exception e) {
                    error "Failed to get the latest Docker tag: ${e.message}"
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
                            // Tag the built image as latest
                            sh "docker tag $DOCKER_IMAGE:$VERSION $DOCKER_IMAGE:latest"
                        } else {
                            bat "docker-compose up --build -d"
                            // Tag the built image as latest
                            bat "docker tag $DOCKER_IMAGE:$VERSION $DOCKER_IMAGE:latest"
                        }
                    }
                }
            }
        }
        stage('Tag & Push Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh "docker tag $DOCKER_IMAGE:latest $NEW_IMAGE"
                        sh "docker push $NEW_IMAGE"
                    } else {
                        bat "docker tag $DOCKER_IMAGE:latest $NEW_IMAGE"
                        bat "docker push $NEW_IMAGE"
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
