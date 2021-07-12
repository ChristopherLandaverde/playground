<template>
    <div class="page-clients">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/ideas" aria-current="true">Inverted Ideas</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Inverted Idea </h1>
                <router-link :to="{ name: 'AddInvertIdea'}" class="button is-light mt-4"> Add Inverted Idea </router-link>

            </div>

            <div
                class="column is-3"
                v-for="invert in inverts"
                v-bind:key="invert.id"
            >
                <div class="box">
                    <h3 class="is-size-4 mb-4"><strong>Idea:</strong> {{ invert.idea }}</h3>
                     <h3 class="is-size-4 mb-4"><strong>Reversed:</strong>  {{ invert.reversed_idea }}</h3>
                      <h3 class="is-size-4 mb-4"><strong>Solution:</strong> {{ invert.wrong }}</h3>
                    <router-link :to="{ name:'InvertedIdea', params: {id: invert.id} }" 
                    class="button is-light">Details</router-link>
                


                   
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'InvertIdea',
    data() {
        return {
            inverts: []
        }
    },
    mounted() {
        this.getIdeas()
    },
    methods: {
        getIdeas() {
            axios
                .get('/api/v1/inverts/')
                .then(response => {
                    console.log(response)
                    for (let i = 0; i < response.data.length; i++) {
                        this.inverts.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
