import * as FilePond from 'filepond'; 
import FilePondPluginImagePreview from 'filepond-plugin-image-preview';
import FilePondPluginFilePoster from 'filepond-plugin-file-poster';
    
FilePond.registerPlugin(
    FilePondPluginImagePreview,
    FilePondPluginFilePoster,
);
// 建立一個多檔案上傳元件 
const pond = FilePond.create({ multiple: true, name: 'filepond' }); 
// 將它新增到DOM 
document.body.appendChild(pond.element); 