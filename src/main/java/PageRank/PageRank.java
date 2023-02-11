package PageRank;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Vector;

public class PageRank {
    private Map<String, Double> ranks;
    private Map<String, String[]> links;

    public PageRank() {
        ranks = new HashMap<>();
        links = new HashMap<>();
        try {
//            PageRank pageRank = new PageRank();
            File myObj = new File("/home/hduser/Downloads/Final/InvertedIndexProblem 1/InvertedIndexProblem/links.txt");
            Scanner myReader = new Scanner(myObj);
            int index = 0;
            String key = new String();
            Vector<String> values = new Vector<>();
            while (myReader.hasNextLine()){
                String line = myReader.nextLine();
                if (line.equals("###")){
                    index = 0 ;
                    this.addPage(key , values.toArray(new String[0]));
                }
                else{
                    if(index == 0){
                        key = line;
                    }
                    else{
                        values.add(line) ;
                    }
                    index++ ;
                }
            }
            myReader.close();
            this.iterate();
        }
        catch (IOException ex){
            System.out.println(ex.getMessage());
        }

    }

    public void addPage(String url, String[] links) {
        ranks.put(url, 1.0);
        this.links.put(url, links);
    }

    public void iterate() {
        Map<String, Double> newRanks = new HashMap<>();

        for (String url : ranks.keySet()) {
            double rank = ranks.get(url);
            double rankContribution = rank / links.get(url).length;

            for (String link : links.get(url)) {
                newRanks.put(link, newRanks.getOrDefault(link, 0.0) + rankContribution);
            }
        }

        ranks = newRanks;
    }

    public Map<String, Double> getRanks() {
        return ranks;
    }
    public static void main(String[] args){
//            PageRank pageRank = new PageRank();
//            for (String i : pageRank.getRanks().keySet()) {
//
//                System.out.println("key: " + i + " value: " + pageRank.getRanks().get(i));
//            }

    }
}