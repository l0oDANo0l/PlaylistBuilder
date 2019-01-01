import Button from '@material-ui/core/Button';

/*** @jsx React.DOM */
var FirstComponent = React.createClass({
    render: function() {
        return (<div>Hey yo<Button>Loading</Button></div>);
    },
    componentDidMount: function(){
        this.loadPollsFromServer()
    },
});
React.render(<FirstComponent />, document.getElementById('mount-point') );