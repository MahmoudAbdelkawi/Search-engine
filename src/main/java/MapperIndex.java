import PageRank.PageRank;
import java.io.IOException;
import java.util.Map;
import java.util.StringTokenizer;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;

public class MapperIndex extends  Mapper<LongWritable, Text, Text, Text> {

    private Text keyinfo = new Text();



    private Text valueinfo = new Text();

    private FileSplit split;
    public static String returnLink(String link){

        link = link.replaceAll("--", ":");
        link = link.replaceAll("___", "/");
        link = link.replaceAll(".txt", "");
        return link;
    }
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context) throws IOException, InterruptedException {
        this.split = (FileSplit)context.getInputSplit();


        StringTokenizer tokenizer = new StringTokenizer(value.toString());

        while(tokenizer.hasMoreTokens()) {

            String fileName = this.split.getPath().getName();
            fileName = returnLink(fileName);
            //<word@filename , 1>
            
            //<<word,filename> , 1>
            //System.out.println(pageRank.getRanks().get(fileName));

            this.keyinfo.set(tokenizer.nextToken() + "@" + fileName);

            this.valueinfo.set("1");
            context.write(this.keyinfo, this.valueinfo);
        }

    }

}
