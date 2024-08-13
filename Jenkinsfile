pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shalomeliy/main_score'
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
        stage('Read Version') {
            steps {
                dir('World_of_Games') {
                    script {
                        version = readFile('version.txt').trim()
                        echo "Current version is ${version}"
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
                        sh "docker tag $DOCKER_IMAGE:${version} shalomeli/world_of_games:${version}"
                        sh "docker push shalomeli/world_of_games:${version}"
                    } else {
                        bat "docker tag $DOCKER_IMAGE:${version} shalomeli/world_of_games:${version}"
                        bat "docker push shalomeli/world_of_games:${version}"
                    }
                }
            }
        }
        stage('Increment Version') {
            steps {
                dir('World_of_Games') {
                    script {
                        def newVersion = version.toInteger() + 1
                        writeFile file: 'version.txt', text: newVersion.toString()
                        echo "New version is ${newVersion}"
                        // Commit and push the new version to the repository
                        if (isUnix()) {
                            sh """
                                git config user.name "Jenkins"
                                git config user.email "jenkins@example.com"
                                git add version.txt
                                git commit -m "Bump version to ${newVersion}"
                                git push origin main
                            """
                        } else {
                            bat """
                                git config user.name "Jenkins"
                                git config user.email "jenkins@example.com"
                                git add version.txt
                                git commit -m "Bump version to ${newVersion}"
                                git push origin main
                            """
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

