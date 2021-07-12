<template>
    <div class="page-clients">
        <nav class="breadcrumb" aria-label="breadcrumbs">
            <ul>
                <li><router-link to="/dashboard">Dashboard</router-link></li>
                <li class="is-active"><router-link to="/ideas" aria-current="true">Cubed Ideas</router-link></li>
            </ul>
        </nav>

        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cubing</h1>
                <router-link :to="{ name: 'AddCubing'}" class="button is-light mt-4"> Add Cubed Idea </router-link>

            </div>

            <div
                class="column is-3"
                v-for="idea in cubedIdeas"
                v-bind:key="idea.id"
            >
                <div class="box">
                    <h2 class="is-size-4 mb-4"> <strong>Analyzed Idea: </strong>  {{ idea.described_idea }}</h2>
                    <router-link :to="{ name:'CubedIdea', params: {id: idea.id}}" 
                    class="button is-light">Details</router-link>
                


                   
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'

export default {
    name:'AddCubed',
    data(){
        return {
            cubedIdeas:[]
        }
    },
    mounted() {
        this.getCubedIdeas()
    },
    methods: {
        getCubedIdeas() {
            axios
                .get('/api/v1/cubing/')
                .then(response => {
                    console.log(response)
                    for (let i = 0; i < response.data.length; i++) {
                        this.cubedIdeas.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        }
    }
}
</script>
