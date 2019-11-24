export default class PDFJs{
    init=(source, element) =>{
        const textNode=document.createElement('p');
        textNode.innerHTML= 'Transcript:${source}';
        if (textNode != null && element != null) {
            element.appendChild(textNode);
        }
        
    }
}