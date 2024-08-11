pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'shalomeliy/world_of_games'
        DOCKER_REGISTRY = 'https://hub.docker.com/repository/docker/shalomeli/world_of_games/tags'
        VERSION = '' // Will be dynamically set in the Increment Version stage
        NEW_IMAGE = '' // Will be set before pushing the image
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
        
