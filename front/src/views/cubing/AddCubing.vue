<template>

<div class="column is-12">


  <div class="container">
  <h1 class="title">Described Ideas</h1>
  <h2 class="subtitle">
    How would you describe this topic, challenge or issue, including characteristics, definitions and parameters?</h2>
    <div class="control">
        <textarea  v-model="cubing.described_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<br>

<div class="container">
  <h1 class="title">Compare your Idea</h1>
  <h2 class="subtitle">
     What is it similar to? Different from?

   </h2>
    <div class="control">
        <textarea  v-model="cubing.compared_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
</div>

<br>
  <div class="container">
  <h1 class="title">Associate your Idea</h1>
  <h2 class="subtitle">
    How does the topic connect to other issues you’ve dealt with before? Does it make you think of anything you’ve worked on in the past? </h2>
    <div class="control">
        <textarea  v-model="cubing.associate_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<br>
 <div class="container">
  <h1 class="title">Analyzed Idea</h1>
  <h2 class="subtitle">
 What smaller parts make up the whole? Is it possible to break down the issue? </h2>
    <div class="control">
        <textarea  v-model="cubing.analyzed_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
 </div>
 <br>


 <div class="container">
  <h1 class="title">Applied your Idea</h1>
  <h2 class="subtitle">
   How is it used? Who uses it?. </h2>
    <div class="control">
        <textarea  v-model="cubing.applyed_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
 </div>
 <br>
  <div class="container">
  <h1 class="title">Argued your Idea</h1>
  <h2 class="subtitle">
  Explain your position for supporting or not supporting it.</h2>
    <div class="control">
        <textarea  v-model="cubing.argued_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
 </div>
 <br>

 <div class="field is-grouped">
  <div class="control">
    <button class="button is-link" @click ="submitForm">Submit</button>
  </div>
  <div class="control">
    <button class="button is-link is-light">Cancel</button>
  </div>
 
 </div>
 


</div>
 

</template>



<script>
import axios from 'axios'
import {toast} from 'bulma-toast'

export default {
    name:'AddCubing',
    data(){
      return{
        cubing:{}
      }

    },
    methods: {
      submitForm(){
            axios
            .post("api/v1/cubing/",this.cubing)
            .then(response=>{
              console.log(response)
                             toast({
                    message:'The Ideas was Added',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover:true,
                    duration:2000,
                    position: 'bottom-right',
                })
                this.$router.push('/cubing')

            
            }).catch(error=>{
                console.log(JSON.stringify(error))
            })
           
      }
    }
}
</script>
