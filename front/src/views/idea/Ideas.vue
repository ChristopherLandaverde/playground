<template>
    <div class="page-clients">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/ideas" aria-current="true">Brain Ideas</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Brain Ideas</h1>
                <router-link :to="{ name: 'AddIdea'}" class="button is-light mt-4"> Add Idea </router-link>

            </div>

            <div
                class="column is-3"
                v-for="idea in ideas"
                v-bind:key="idea.id"
            >
                <div class="box">
                    <h3 class="is-size-4 mb-4">{{ idea.goals }}</h3>
                    <router-link :to="{ name:'Idea', params: {id: idea.id}}" 
                    class="button is-light">Details</router-link>
                


                   
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Ideas',
    data() {
        return {
            ideas: []
        }
    },
    mounted() {
        this.getIdeas()
    },
    methods: {
        getIdeas() {
            axios
                .get('/api/v1/brainstorms/')
                .then(response => {
                    console.log(response)
                    for (let i = 0; i < response.data.length; i++) {
                        this.ideas.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>