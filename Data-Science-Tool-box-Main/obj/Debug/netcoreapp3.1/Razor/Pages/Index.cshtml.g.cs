#pragma checksum "C:\Users\YOUYANG ZHOU\Desktop\Cloud-computing\Term-Project\Cloud-Term-Project-Microservices\Data-Science-Tool-box-Main\Pages\Index.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "dd308028ddb0a8765b1f3065668a2fa1e2316318"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(Data_Science_Tool_box_Main.Pages.Pages_Index), @"mvc.1.0.razor-page", @"/Pages/Index.cshtml")]
namespace Data_Science_Tool_box_Main.Pages
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "C:\Users\YOUYANG ZHOU\Desktop\Cloud-computing\Term-Project\Cloud-Term-Project-Microservices\Data-Science-Tool-box-Main\Pages\_ViewImports.cshtml"
using Data_Science_Tool_box_Main;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"dd308028ddb0a8765b1f3065668a2fa1e2316318", @"/Pages/Index.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"5063c3578dcabafcd5ffea8156c2ef0b8651aa98", @"/Pages/_ViewImports.cshtml")]
    public class Pages_Index : global::Microsoft.AspNetCore.Mvc.RazorPages.Page
    {
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
#nullable restore
#line 3 "C:\Users\YOUYANG ZHOU\Desktop\Cloud-computing\Term-Project\Cloud-Term-Project-Microservices\Data-Science-Tool-box-Main\Pages\Index.cshtml"
  
    ViewData["Title"] = "Home page";

#line default
#line hidden
#nullable disable
            WriteLiteral(@"
<div class=""text-center"">
    <h1 class=""display-4"">Welcome to Data Science Tool Box</h1>
    <p>Please run one of the following applications</p>
    <p><a href=""http://localhost:8787"">RStudio</a></p>
    <p><a href=""http://localhost:6080/vnc.html?resize=downscale&autoconnect=1&password=secret"">Spyder</a></p>
    <p>If the above link fail to work, use this one for SpyderIDE
    instead<br /><a href=""https://mybinder.org/v2/gh/spyder-ide/spyder/master?urlpath=%2Fdesktop"">Spyder-Backup</a></p>
    <p><a href=""https://welcome.oda.sas.com/login"">IBM SAS</a></p>
    <p><a href=""http://localhost:8008/vnc.html"">Git</a></p>
    <p><a href=""http://localhost:8888"">Jupyter Notebook</a></p>
    <p><a href=""http://localhost:6901"">Orange</a></p>
    <p><a href=""http://localhost:8443"">Visual Studio Code IDE</a></p>
    <p><a href=""http://localhost:8081/vnc.html"">Apache Hadoop</a></p>
    <p><a href=""http://localhost:8082/vnc.html"">Apache Spark</a></p>
    <p><a href=""https://prod-useast-b.online.tableau.com/");
            WriteLiteral(@"#/site/yryoliverattableaucom/home"">Tableau</a></p>
    <p><a href=""http://localhost:9000/dashboard?id=MyProjectKey"">SonarQube and Sonar Scanner Binaries</a></p>
    <p><a href=""http://localhost:8083/vnc.html"">Tensorflow</a></p>
    <p><a href=""http://localhost:8080"">Markdown-Dillinger Eiditor</a></p>
    <p><a href=""https://localhost:44382/NotePadStart"">Notepad++</a></p>
</div>
");
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<IndexModel> Html { get; private set; }
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.ViewDataDictionary<IndexModel> ViewData => (global::Microsoft.AspNetCore.Mvc.ViewFeatures.ViewDataDictionary<IndexModel>)PageContext?.ViewData;
        public IndexModel Model => ViewData.Model;
    }
}
#pragma warning restore 1591
