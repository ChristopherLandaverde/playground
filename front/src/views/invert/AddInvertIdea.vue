<template>


<div class="column is-12">


  <div class="container">
  <h1 class="title">Idea</h1>
  <h2 class="subtitle">
    Without Thinking, write simply an idea you're contemplating. For an example: <strong> "How do we imporve the customer call center experience?"</strong>  </h2>
    <div class="control">
        <textarea  v-model="invertedideas.idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<br>
<div class="container">
  <h1 class="title">Reversed Idea</h1>
  <h2 class="subtitle">
    Now keep that thought and reverse it completely. For an example: <strong>“How can we make the customer call center experience a more dissatisfying one? </strong> </h2>
    <div class="control">
        <textarea  v-model="invertedideas.reversed_idea" class="textarea" placeholder="Textarea"></textarea>
        </div>
</div>
<br>
  <div class="container">
  <h1 class="title">Any Ideas that you can take from this?</h1>
  <h2 class="subtitle">
    Write some thoughts based on this. For an example: <strong>“Resolve customer inquiries effectively and efficiently, without putting them on hold?"" </strong>. </h2>
    <div class="control">
        <textarea  v-model="invertedideas.wrong" class="textarea" placeholder="Textarea"></textarea>
        </div>
  </div>
<br>


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
    name:'AddInvertIdea',
    data(){
        return {
            invertedideas:{}
        }
    },
    methods:{
        submitForm(){
            axios
            .post("api/v1/inverts/",this.invertedideas)
            .then(response=>{
                             toast({
                    message:'The Ideas was Added',
                    type: 'is-success',
                    dismissible: true,
                    pauseOnHover:true,
                    duration:2000,
                    position: 'bottom-right',
                })

                this.$router.push('/invert')
            }).catch(error=>{
                console.log(JSON.stringify(error))
            })
        }
    }
}
</script>
