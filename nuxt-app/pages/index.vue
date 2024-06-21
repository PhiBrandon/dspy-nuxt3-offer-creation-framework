<template>
    <div class="flex flex-col justify-center mx-auto items-center max-w-7xl min-h-screen">
        <header class="mt-24">
            <h1 class="text-2xl font-bold">Offer Generator</h1>
        </header>
        <div class="w-96 mt-12">
            <form class="flex flex-col" @submit.prevent="sendInformation">
                <textarea class="textarea textarea-bordered" placeholder="Customer Problem" v-model="job"></textarea>
                <button class="btn btn-lg">Generate</button>
            </form>
        </div>
        <div v-if="loading" class="text-center mt-4">
            <p>Generating Sweet Offers...</p>
            <span class="loading loading-spinner text-info"></span>
        </div>
        <div v-else-if="error">
            Something went wrong, try again.
        </div>
        <content v-else class="flex flex-wrap justify-center">
            <div v-for="({ problem }, index) in json.problem" class="my-4">
                <div class="card max-w-full bg-base-100 shadow-xl">
                    <div class="card-body">
                        <!-- Card Header -->
                        <h2 class="text-lg">Problem: {{ problem }}</h2>
                        <!-- Sub Problems -->
                        <div>
                            <div class="collapse collapse-arrow bg-base-200">
                                <input type="checkbox" name="my-accordion-2" />
                                <div class="collapse-title text-xl font-medium">
                                    Sub Problems
                                </div>
                                <div class="collapse-content">
                                    <ul v-for="(sub, inex) in json.sub_problems[index]">
                                        <li>{{ inex + 1 }} . {{ sub.sub_problems }}</li>
                                    </ul>

                                </div>
                            </div>
                        </div>
                        <!-- Objections -->
                        <div>
                            <div class="collapse collapse-arrow bg-base-200">
                                <input type="checkbox" name="my-accordion-2" />
                                <div class="collapse-title text-xl font-medium">
                                    Objections
                                </div>
                                <div class="collapse-content">
                                    <ul v-for="(object, inex) in json.objections[index]">
                                        <li>{{ inex + 1 }} . {{ object.objection }}</li>
                                    </ul>

                                </div>
                            </div>
                        </div>
                        <!-- Solutions -->
                        <div>
                            <div class="collapse collapse-arrow bg-base-200">
                                <input type="checkbox" name="my-accordion-2" />
                                <div class="collapse-title text-xl font-medium">
                                    Solutions
                                </div>
                                <div class="collapse-content space-y-2">
                                    <!-- Solutions Table -->
                                    <div class="space-y-4 collapse collapse-arrow">
                                        <input type="checkbox" name="my-accordion-2" />
                                        <h1 class="text-lg font-bold collapse-title">Do it yourself</h1>
                                        <div class="collapse-content">
                                            <ul class=""
                                                v-for="(solutions, idx) in json.solutions[index].do_it_yourself_solutions">
                                                <li>{{ idx + 1 }}. {{ solutions }} </li>
                                            </ul>
                                        </div>

                                    </div>
                                    <div class="space-y-4 collapse collapse-arrow">
                                        <input type="checkbox" name="my-accordion-2" />
                                        <h1 class="text-lg font-bold collapse-title">Done for you</h1>
                                        <div class="collapse-content">
                                            <ul class=""
                                                v-for="(solutions, idx) in json.solutions[index].done_for_you_solutions">
                                                <li>{{ idx + 1 }}. {{ solutions }} </li>
                                            </ul>
                                        </div>

                                    </div>
                                    <div class="space-y-4 collapse collapse-arrow">
                                        <input type="checkbox" name="my-accordion-2" />
                                        <h1 class="text-lg font-bold collapse-title">Done with you</h1>
                                        <div class="collapse-content">
                                            <ul class=""
                                                v-for="(solutions, idx) in json.solutions[index].done_with_you_solutions">
                                                <li>{{ idx + 1 }}. {{ solutions }} </li>
                                            </ul>
                                        </div>

                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
            <!-- Loop through problems and generate a div -->
        </content>

    </div>
</template>


<script setup="ts">
let job = ref("")
let loading = ref(false)
let error = ref(false)
async function sendInformation(e) {
    console.log("Sending")
    loading.value = true
    let data = await $fetch('api/generate', {
        method: 'POST',
        body: { job: job.value }
    }).catch((out) => {
        error.value = true
        loading.value = false
    })
    if (data) {
        json.value = data
        loading.value = false
    }

}
let json = ref({})
</script>