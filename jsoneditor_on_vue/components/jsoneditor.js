Vue.component('jsoneditor', {
    template:
    `<canvas  v-bind:id="jp_props.id" :class="jp_props.classes"  :style="jp_props.style" :width="jp_props.width" height="jp_props.height"></canvas>`,
    methods: {
        content_change() {
            console.log("graph change");
            var id = this.$props.jp_props.id.toString();
            // launch a new editor
	    const container = 	document.getElementById(id);
	const options = {};
	const editor = new JSONEditor(container, options);
	const initialJson = {
            "Array": [1, 2, 3],
            "Boolean": true,
            "Null": null,
            "Number": 123,
            "Object": {"a": "b", "c": "d"},
            "String": "Hello World"
        }
		console.log(this.$props.jp_props.jsontext)
        editor.set(initialJson)


        },
        editor_destroy() {
            var id = this.$props.jp_props.id.toString();
            //destroy existing editor
        }
    },
    
    mounted() {
        console.log("mounted");
        this.content_change();
    },
    updated() {
        console.log("updated called");
        const container = this.$props.jp_props.id.toString();
        if (this.$props.jp_props.update_create) {
                //console.log("this is a new graph")
                this.editor_destroy();
                this.editor_change();
            } else {
                //console.log("this is an update")
                this.editor_change()
                //chart.update(this.$props.jp_props.def, true, true, this.$props.jp_props.update_animation); //Look into chart.update
            }

    },
    props: {
        jp_props: Object
    }
});
