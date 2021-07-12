<template>
<div class="page-dashboard">
    <div class="columns is-multiline">
        <div class="column is-12">
      
           

                <div class="container">
                      <div class="notification is-primary">

                    <h1 class="title is-1"> Last Three Cubed Ideas </h1>
                    <div
                class="column is-3"
                v-for="cube in cubes"
                v-bind:key="cube.id"
                >
                    <h4 class="title is-4">  {{ cube.associate_idea }}</h4>
                    
                    
                </div>
                <button class="button is-white">
                <router-link to="/cubing" >See More</router-link>
                </button>
                 </div>
             </div>

                <br>

                <div class="container">
                     <div class="notification is-info">
                    <h1 class="title is-1"> Last Three Brain Ideas  </h1>
                    <div
                class="column is-3"
                v-for="brain in brainstorms"
                v-bind:key="brain.id">
                     <h4 class="title is-4"> {{ brain.goals }}</h4>                
                </div>

                    <button class="button is-white">
                <router-link to="/ideas">See More</router-link>
                </button>
                 </div>

                </div>

<br>
                <div class="container">
                     <div class="notification is-light">
                    <h1 class="title is-1"> Last Three Inversions Ideas  </h1>
                    <div
                class="column is-3"
                v-for="brain in brainstorms"
                v-bind:key="brain.id">
                     <h4 class="title is-4"> {{ brain.goals }}</h4>                
                </div>

                    <button class="button is-white">
                <router-link to="/inverts">See More</router-link>
                </button>
                 </div>

                </div>
            </div>
               
            
       
     
    </div>
</div>
    
</template>

<script>
import axios from 'axios'

export default {
    name: 'Dashboard',
    data(){
        return{
            cubes:[],
            brainstorms:[],
            inversions:[]

        }
    },
    async mounted() {
        await this.getCubed()
        await this.getBrainStorm()
        await this.getInversions()
        
   
    },
    methods: {
        getCubed(){
                  axios
                .get('/api/v1/cubing/')
                .then(response => {
                    console.log(response)
                    for (let i = 3 - 1; i >= 0; i--) {
                        this.cubes.push(response.data[i])
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        getBrainStorm(){
                axios
                .get('/api/v1/brainstorms/')
                .then(response => {
                    console.log(response.data)
                     for (let i = 3 - 1; i >= 0; i--) {
                        this.brainstorms.push(response.data[i])
                     
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })
        },
        getInversions(){
                           axios
                .get('/api/v1/inverts/')
                .then(response => {
                    console.log(response.data)
                     for (let i = 3 - 1; i >= 0; i--) {
                        this.inversions.push(response.data[i])
                     
                    }
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })


        }
    }

}
</script>
